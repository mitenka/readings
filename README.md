# Installation

* Clone the repository.
* Change to the application folder. 
* Checkout (if not yet) `develop` branch.
* Build Docker image and run its container like following.

```
$ docker build -t readings .
$ docker run -p 8080:8080/tcp readings
```

# API Reference

## Objects
### Reading
* `id : Integer`
* `value : Float`
* `timestamp : DateTime`

## Endpoints
#### Create reading
```
POST /readings/

{
  "value": "1.1"
}
```

> Please note that quotes for float values are used by design.

##### Parameters
* `value : Float`

##### Statuses
* 200, Success
* 400, Bad request

#### Get paginated reading list
```
GET /readings/
```
##### Statuses
* 200, Success

#### Retrieve reading
```
GET /readings/:id/
```

##### Path parameters
* `id : Integer`

##### Statuses
* 200, Success
* 404, Not found

#### Update reading
```
PUT /readings/:id/

{
  "value": "5.55"
}
```

> Please note that quotes for float values are used by design.

##### Parameters
* `value : Float`

##### Path parameters
* `id : Integer`

##### Statuses
* 200, Success
* 400, Bad request
* 404, Not found

#### Delete reading
```
DELETE /readings/:id/
```

##### Path parameters
* `id : Integer`

##### Statuses
* 204, No content
* 404, Not found

#### Statistics
```
GET /statistics/
```

> Please note that quotes for float values are used by design.

##### Statuses
* 200, Success
