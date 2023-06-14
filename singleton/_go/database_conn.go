package main

import "fmt"

type DatabaseConnection struct {
	Connection string
}

var instance_ *DatabaseConnection

func NewConnection() *DatabaseConnection {
	if instance_ == nil {
		instance_ = &DatabaseConnection{}
	}
	return instance_
}

func (db *DatabaseConnection) Connect(databaseName string) string {
	if db.Connection == "" {
		db.Connection = databaseName
	}
	return db.Connection
}

func (db *DatabaseConnection) Close() {
	if instance_ != nil {
		instance_.Connection = ""
		instance_ = nil
	}
}

func main() {
	dbManager1 := NewConnection()
	dbManager2 := NewConnection()

	conn1 := dbManager1.Connect("NasDB")
	conn2 := dbManager2.Connect("SifatDB")
	fmt.Println(conn1 == conn2) // Outputs: true

	dbManager1.Close()
	conn3 := dbManager2.Connect("PiluDB")
	fmt.Println(conn1 == conn3) // Outputs: false
}
