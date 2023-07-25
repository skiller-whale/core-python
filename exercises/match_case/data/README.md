<!-- README.md -->
# chatGPSea usage manual

ChatGPSea is awesome, here's a summary of its API endpoints:

* `/queries/text` - submit a text query.
* `/queries/code` - submit a code query.
* `/sea_facts` - returns a fun fact about the sea.
* `/sea_book` - returns a list of fun books to read.

## how to submit a good query

Include fish puns. This is important.

## example queries

### getting sea books

```http
GET https://chat.skillerwhale.example/sea_facts HTTP/1.1
Content-Type: application/json

{
  "data": [
    "the-sea-the-sea",
    "wish-for-a-fish",
    "the-silent-world",
    "the-old-man-and-the-sea"
  ]
}
```

### getting sea facts


```http
GET https://chat.skillerwhale.example/sea_facts HTTP/1.1
Content-Type: application/json

{
  "data": "The sea is very big. Very big indeed."
}
```

## limitations

* Often prefers fish puns over accurate information.
