package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

func readFile(filename string) (lines []string) {
	dat, _ := ioutil.ReadFile("input")
	lines = strings.Split(string(dat), "\n")
	return
}

func condition(val1 int, cond string, val2 int) bool {
	if cond == ">" {
		return val1 > val2
	}
	if cond == "<" {
		return val1 < val2
	}
	if cond == ">=" {
		return val1 >= val2
	}
	if cond == "<=" {
		return val1 <= val2
	}
	if cond == "==" {
		return val1 == val2
	}
	if cond == "!=" {
		return val1 != val2
	}
	return false
}

func execute(instructions []string, registers map[string]int) {
	r, _ := regexp.Compile("^([a-z]+) (inc|dec) ([0-9-]+) if ([a-z]+) ([!<>=]+) ([0-9-]+)$")
	for _, line := range instructions {
		res := r.FindAllStringSubmatch(line, -1)[0]
		condVal, _ := strconv.Atoi(res[6])
		if condition(registers[res[4]], res[5], condVal) {
			val, _ := strconv.Atoi(res[3])
			if res[2] == "inc" {
				registers[res[1]] += val
			}
			if res[2] == "dec" {
				registers[res[1]] -= val
			}
			if registers[res[1]] > registers["_biggest"] {
				registers["_biggest"] = registers[res[1]]
			}
		}
	}
}

func main() {

	lines := readFile("input")

	registers := make(map[string]int)

	execute(lines, registers)

	biggestVal := 0
	for k, v := range registers {
		if k != "_biggest" && v > biggestVal {
			biggestVal = v
		}
	}
	fmt.Println(biggestVal)
	fmt.Println(registers["_biggest"])

}
