package main

import "fmt"

//var once sync.Once

type SingleTon struct {
	name string
}

var instance *SingleTon

func GetInstance() *SingleTon {
	//once.Do(func() {
	//	instance = &SingleTon{}
	//})
	if instance == nil {
		instance = &SingleTon{
			name: "Sifat",
		}
	}
	return instance
}

func main() {
	instance := GetInstance()
	// Use the singleton instance
	fmt.Println(instance)
	instance2 := GetInstance()
	fmt.Println(instance2)
}
