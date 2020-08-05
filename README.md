# Rarbg-API
A simple search API for Rarbg

---

## Usage

Make a get request specifying the search query
```
https://rarbg-api.herokuapp.com/search?q={string}
```
Example - https://rarbg-api.herokuapp.com/search?q=ubuntu

---

## Response Format

The response JSON Object looks something like this - 

```JSON
{
  "success": true,
  "data": [
    {
      "title": "Aerial.Africa.Series.1.2of6.Spirit.of.Ubuntu.1080p.HDTV.x264.AAC.MVGroup.or",
      "size": "1.50 GB",
      "seeds": "4",
      "leeches": "1",
      "uploader": "Harry65",
      "magnet": "magnet:?xt=nce&tr=udp%3A%2F%2F9.rarbg.me%3A2760&tr=udp%3A%2F%2F9.rarbg.to%3A2800"
    },
    {
      "title": "Ubuntu 11 10 Install Box",
      "size": "3.72 GB",
      "seeds": "1",
      "leeches": "1",
      "uploader": "Harry65",
      "magnet": "magnet:?xt=&tr=udp%3A%2F%2F9.rarbg.me%3A2760&tr=udp%3A%2F%2F9.rarbg.to%3A2800"
    }
  ]
}
```

---

## Setup

Install all dependencies listed in *requirements.txt* file. 

1. To install all dependencies run - 

    ```bash
    $ sudo -H pip3 install -r requirements.txt
    ```

2. Start the server

    ```bash 
    $ python app.py
    ```

---

### Deploy it on Heroku :)  
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/confident-hate/Rarbg-API/tree/master)

---

#### Star the Repo in case you liked it :)
