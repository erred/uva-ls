package main

import (
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"net/http"
	"net/url"
	"os"
	"path/filepath"
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
				log.Println("rate limited, sleeping for 1min")
				time.Sleep(1 * time.Minute)
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
				log.Println("rate limited, sleeping for 1min")
				time.Sleep(1 * time.Minute)
				continue
			}
			log.Println("download link other err")
			i++
			continue
		}
		data[i] = append(data[i], dl.String())
	}

	f, err = os.Create("photos-dl.csv")
	if err != nil {
		log.Printf("create file: %v", err)
		return
	}
	defer f.Close()

	w = csv.NewWriter(f)
	w.WriteAll(data)
	w.Flush()
	fmt.Printf("written %d records\n", len(data))

	os.Mkdir("./photos", 0755)
	for i := 0; i < len(data); {
		func() {
			res, err := client.Get(data[i][3])
			if err != nil {
				log.Printf("download %d err: %v, sleeping for 1 min\n", i, err)
				time.Sleep(time.Minute)
				return
			}
			defer res.Body.Close()
			i++
			u, err := url.Parse(data[i][3])
			if err != nil {
				log.Printf("parse %d url: %v\n", i, err)
				return
			}
			fp := "./photos/" + filepath.Base(u.Path)
			f, err := os.Create(fp)
			if err != nil {
				log.Println("create file %d %s err: %v\n", i, fp, err)
				return
			}
			defer f.Close()
			io.Copy(f, res.Body)
		}()
	}
}
