package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

type layer struct {
	d int
	r int
}

func caughtInFirewall(firewall []layer, delay int) bool {

	for _, l := range firewall {
		if (l.d+delay)%(l.r*2-2) == 0 {
			return true
		}
	}
	return false
}

func main() {

	scanner := bufio.NewScanner(os.Stdin)

	r, _ := regexp.Compile("^([0-9]+): ([0-9]+)$")

	total := 0
	firewall := make([]layer, 0)

	for scanner.Scan() {
		line := scanner.Text()
		res := r.FindAllStringSubmatch(line, -1)[0]
		d, _ := strconv.Atoi(res[1])
		r, _ := strconv.Atoi(res[2])
		firewall = append(firewall, layer{d: d, r: r})

		if d%(r*2-2) == 0 {
			total += d * r
		}

	}

	fmt.Println(total)

	for i := 0; ; i++ {
		if !caughtInFirewall(firewall, i) {
			fmt.Println(i)
			break
		}
	}

}
