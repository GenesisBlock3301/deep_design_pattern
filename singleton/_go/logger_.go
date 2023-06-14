package main

import "fmt"

type Logger struct {
	Message string
}

var _instance *Logger

func NewLogger() *Logger {
	if _instance == nil {
		_instance = &Logger{}
	}
	return _instance
}

func (l *Logger) Log(message string) {
	l.Message = message
	fmt.Println(l.Message)
}

func main() {
	l1 := NewLogger()
	l2 := NewLogger()
	fmt.Println(l1 == l2)
	l1.Log("Message 1")
	l2.Log("Message 2")
}
