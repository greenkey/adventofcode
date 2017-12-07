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

func parseProgramNote(note string) (p Program) {
	r, _ := regexp.Compile("^([^ ]+) \\(([0-9]+)\\)( -> (.*))?$")
	res := r.FindAllStringSubmatch(note, -1)[0]
	p.Name = res[1]
	p.Weight, _ = strconv.Atoi(res[2])
	p.SubProgramNames = strings.Split(res[4], ", ")
	return
}

type Program struct {
	Name            string
	Weight          int
	SubProgramNames []string
	Parent          *Program
}

func remove(s []string, i int) []string {
	s[len(s)-1], s[i] = s[i], s[len(s)-1]
	return s[:len(s)-1]
}

func main() {

	lines := readFile("input")
	r, _ := regexp.Compile("[a-z]+")
	programMentions := make(map[string]int)
	for _, line := range lines {
		for _, name := range r.FindAllString(line, -1) {
			programMentions[name]++
		}
	}

	for name, mentions := range programMentions {
		if mentions == 1 {
			fmt.Println(name)
			break
		}
	}

}
