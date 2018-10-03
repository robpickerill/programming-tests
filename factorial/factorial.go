package main

import (
	"fmt"
)

// factorial is a recursive function to return factorial of num
func factorial(num int) int {
	if num == 0 {
		return 1
	}
	return num * factorial(num-1)
}

func main() {
	fmt.Println(factorial(3))
}
