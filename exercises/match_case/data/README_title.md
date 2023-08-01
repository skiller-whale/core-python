<!-- README.md -->
# Chatgpsea Usage Manual

ChatGPSea is awesome, here's a summary of its API endpoints:

* `/queries/text` - submit a text query.
* `/queries/code` - submit a code query.
* `/sea_facts` - returns a fun fact about the sea.
* `/sea_book` - returns a list of fun books to read.

## How To Submit A Good Query

Include fish puns. This is important.

## Example Queries

### Getting Sea Books

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

### Getting Sea Facts


```http
GET https://chat.skillerwhale.example/sea_facts HTTP/1.1
Content-Type: application/json

{
  "data": "The sea is very big. Very big indeed."
}
```

## Limitations

* Often prefers fish puns over accurate information.
