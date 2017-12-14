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

func KHashString(s string) string {
	list := make([]int, 256)
	for i := range list {
		list[i] = i
	}
	suffix := []rune{17, 31, 73, 47, 23}

	sequence := s + string(suffix)

	var pos, skip int
	for i := 0; i < 64; i++ {
		for _, c := range sequence {
			slice := make([]int, c)
			for j := 0; j < int(c); j++ {
				slice[j] = list[(pos+j)%len(list)]
			}

			for j := 0; j < int(c); j++ {
				list[(pos+j)%len(list)] = slice[len(slice)-j-1]
			}

			pos += (int(c) + skip)
			skip++
		}
	}

	denseHash := make([]int, 16)
	for i := range denseHash {
		x := i * 16
		for j := 0; j < 16; j++ {
			denseHash[i] = denseHash[i] ^ list[x+j]
		}
	}

	ret := ""
	for i := range denseHash {
		ret += fmt.Sprintf("%02x", denseHash[i])
	}

	return ret
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

		fmt.Println(KHashString(line))

	}

}
