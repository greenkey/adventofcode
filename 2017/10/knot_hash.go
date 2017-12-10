package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func KHash(size int, ints []int) (hash int) {
	list := make([]int, size)
	for i := 0; i < size; i++ {
		list[i] = i
	}

	pos := 0
	skip := 0
	for _, n := range ints {
		slice := make([]int, n)
		for j := 0; j < n; j++ {
			slice[j] = list[(pos+j)%len(list)]
		}

		reverseSlice := make([]int, n)
		for j := range slice {
			reverseSlice[j] = slice[len(slice)-j-1]
		}

		for j := 0; j < n; j++ {
			list[(pos+j)%len(list)] = reverseSlice[j]
		}

		pos += n + skip
		skip++
	}

	return list[0] * list[1]

}

func main() {

	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		line := scanner.Text()
		intStrings := strings.Split(line, ",")
		intInts := make([]int, len(intStrings))
		for i, n := range intStrings {
			intInts[i], _ = strconv.Atoi(n)
		}
		fmt.Println(KHash(256, intInts))
	}

}
