package main

import (
	"bufio"
	"fmt"
	"os"
)

func getStreamScore(s string) (score, removed int) {
	var level int
	skip := false
	garbage := false
	for _, c := range s {
		if skip {
			skip = false
			continue
		}

		if c == '!' {
			skip = true
			continue
		}

		if c == '>' {
			garbage = false
		}
		if garbage {
			removed++
			continue
		}
		if c == '<' {
			garbage = true
		}

		if c == '{' {
			level++
		}
		if c == '}' {
			score += level
			level--
		}
	}
	return
}

func main() {

	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		fmt.Println(getStreamScore(scanner.Text()))
	}

}
