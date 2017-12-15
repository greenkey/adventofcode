package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

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

func hex2bin(hex string) (bin string) {
	for i := range hex {
		n, err := strconv.ParseUint(hex[i:i+1], 16, 32)
		if err != nil {
			panic(err)
		}
		bin += fmt.Sprintf("%04b", n)

	}
	return
}

func fill(bitmap *[][]rune, x int, y int, filler rune) {
	bm := *bitmap
	if bm[x][y] == -1 {
		bm[x][y] = filler

		if x > 0 {
			fill(bitmap, x-1, y, filler)
		}
		if x < len(bm)-1 {
			fill(bitmap, x+1, y, filler)
		}
		if y > 0 {
			fill(bitmap, x, y-1, filler)
		}
		if y < len(bm[x])-1 {
			fill(bitmap, x, y+1, filler)
		}
	}
}

func main() {

	testString := "a0c2017"
	if hex2bin(testString) != "1010000011000010000000010111" {
		fmt.Println("1010000011000010000000010111")
		fmt.Println(hex2bin(testString))
		panic("")
	}

	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		line := scanner.Text()

		sum := 0
		groups := make([][]rune, 128)
		for i := 0; i < 128; i++ {
			s := fmt.Sprintf("%s-%d", line, i)
			res := hex2bin(KHashString(s))
			groups[i] = []rune(res)
			for j, c := range res {
				groups[i][j] = c - 50
				if c == '1' {
					sum++
				}
			}
		}
		fmt.Println(sum)

		groupsNo := 0
		for i, line := range groups {
			for j, c := range line {
				if c == -1 {
					groupsNo++
					fill(&groups, i, j, rune(groupsNo))
				}
			}
		}
		fmt.Println(groupsNo)

	}

}
