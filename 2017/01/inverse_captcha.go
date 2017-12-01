package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
)

func main() {
	dat, _ := ioutil.ReadFile("input")

	prev := dat[len(dat)-1]
	total := 0
	for _, item := range dat {
		if item == prev {
			i, _ := strconv.Atoi(string(item))
			total += i
		}
		prev = item
	}
	fmt.Println(total)

	halfway := len(dat) / 2

	total = 0
	for i := range dat {
		if dat[i] == dat[(i+halfway)%len(dat)] {
			j, _ := strconv.Atoi(string(dat[i]))
			total += j
		}
	}
	fmt.Println(total)

}
