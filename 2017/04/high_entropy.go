package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strings"
)

func readFile(filename string) (words [][]string) {
	dat, _ := ioutil.ReadFile("input")
	lines := strings.Split(string(dat), "\n")
	for _, line := range lines {
		words = append(words, strings.Split(line, " "))
	}
	return
}

func main() {
	fileContent := readFile("input")
	count := 0

	for _, line := range fileContent {
		words := make(map[string]int)
		duplicates := false
		for _, word := range line {
			_, ok := words[word]
			if ok {
				duplicates = true
				break
			}
			words[word] = 1
		}
		if !duplicates {
			count++
		}
	}

	fmt.Println(count)

	count = 0
	for _, line := range fileContent {
		words := make(map[string]int)
		duplicates := false
		for _, word := range line {
			w := strings.Split(word, "")
			sort.Strings(w)
			word = strings.Join(w, "")
			//fmt.Println(word)
			_, ok := words[word]
			if ok {
				duplicates = true
				break
			}
			words[word] = 1
		}
		if !duplicates {
			count++
		}
	}

	fmt.Println(count)

}
