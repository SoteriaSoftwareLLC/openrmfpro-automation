// test authentication, just using a command line call
// ex: ./authentication http://192.168.13.111:8080 openrmfprosrc hvs.xxxxxxxxxxxxxx

package main

import (
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
	"os"
	"strings"
)

func main() {
	apiPath := os.Args[1] + "/api/external/testauthentication"
	apiKey := os.Args[2]

	// Create a Bearer string by appending string access token
	var bearer = "Bearer " + os.Args[3]

	data := url.Values{}
	data.Set("applicationKey", apiKey)

	// create request
	req, err := http.NewRequest("POST", apiPath, strings.NewReader(data.Encode()))
	if err != nil {
		panic(err)
	}

	// add authorization header to the req
	req.Header.Add("Authorization", bearer)
	req.Header.Add("Accept", "application/json")
	req.Header.Add("Content-Type", "application/x-www-form-urlencoded")

	// send request with headers
	client := &http.Client{}
	resp, err := client.Do(req)

	// //Handle Error
	if err != nil {
		log.Fatalf("An Error Occured %v", err)
	}
	defer resp.Body.Close()

	//Read the response body
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}
	sb := string(body)
	log.Printf(sb)
}
