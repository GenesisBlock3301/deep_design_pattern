package main

import (
	"encoding/json"
	"fmt"
	"reflect"
)

// Marshal: means structure object, you are converting it to its JSON counterpart.
// Unmarshal:  you are trying to convert some JSON-expected-data to a known struct or object

type MyObject struct {
	Number int    `json:"number"`
	Word   string `json:"word"`
}

func main() {
	obj := MyObject{5, "Packet"}
	oJson, _ := json.Marshal(obj)
	var object MyObject
	fmt.Printf("%s\n", reflect.TypeOf(oJson), oJson)

	err := json.Unmarshal(oJson, &object)
	if err != nil {
		panic(err)
	}
	fmt.Println(object.Number, object.Word)
}
