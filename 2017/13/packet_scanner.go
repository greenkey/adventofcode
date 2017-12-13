package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {

	scanner := bufio.NewScanner(os.Stdin)

	r, _ := regexp.Compile("^([0-9]+): ([0-9]+)$")

	total := 0

	for scanner.Scan() {
		line := scanner.Text()
		res := r.FindAllStringSubmatch(line, -1)[0]
		d, _ := strconv.Atoi(res[1])
		r, _ := strconv.Atoi(res[2])

		if d%(r*2-2) == 0 {
			total += d * r
		}

	}

	fmt.Println(total)

}
