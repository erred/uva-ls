package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"net/http"
	"os"
	"strconv"
	"time"

	"github.com/hbagdi/go-unsplash/unsplash"
)

type myTransport struct{}

func (t *myTransport) RoundTrip(req *http.Request) (*http.Response, error) {
	req.Header.Add("authorization", "Client-ID "+os.Getenv("UNSPLASH"))
	return http.DefaultTransport.RoundTrip(req)
}

func main() {
	client := &http.Client{
		Transport: &myTransport{},
	}

	u := unsplash.New(client)
	o := &unsplash.ListOpt{Page: 1, PerPage: 100}
	if !o.Valid() {
		log.Println("options not valid")
	}

	var data [][]string
	defer func() {
		f, err := os.Create("photos-deferred.csv")
		if err != nil {
			log.Printf("create file: %v", err)
			return
		}
		defer f.Close()

		w := csv.NewWriter(f)
		w.WriteAll(data)
		w.Flush()
		fmt.Printf("written %d records\n", len(data))

	}()

	for len(data) < 600 {
		photos, res, err := u.Photos.All(o)
		if err != nil {
			if _, ok := err.(*unsplash.RateLimitError); ok {
				log.Println("rate limited, sleeping for 10min")
				time.Sleep(10 * time.Minute)
				continue
			}
			log.Println("other err: ", err)
			return
		}

		for _, p := range *photos {
			if *p.Width > 4000 && *p.Height > 4000 {
				data = append(data, []string{strconv.Itoa(*p.Width), strconv.Itoa(*p.Height), *p.ID})
			}
		}
		fmt.Println("current count: ", len(data))

		if !res.HasNextPage {
			break
		}
		o.Page = res.NextPage
	}

	f, err := os.Create("photos.csv")
	if err != nil {
		log.Printf("create file: %v", err)
		return
	}
	defer f.Close()

	w := csv.NewWriter(f)
	w.WriteAll(data)
	w.Flush()
	fmt.Printf("written %d records\n", len(data))

	for i := 0; i < len(data); {
		dl, _, err := u.Photos.DownloadLink(data[i][2])
		if err != nil {
			if _, ok := err.(*unsplash.RateLimitError); ok {
				log.Println("rate limited, sleeping for 10min")
				time.Sleep(10 * time.Minute)
				continue
			}
			log.Println("download link other err")
			i++
			continue
		}
		data[i] = append(data[i], dl.String())
	}
}
