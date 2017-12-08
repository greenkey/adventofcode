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

func whosStrange(list []int) (strangeIndex, normal int) {
	if len(list) == 0 {
		return -1, -1
	}
	if len(list) == 1 {
		return -1, list[0]
	}
	if len(list) == 2 && list[0] == list[1] {
		return -1, list[0]
	}
	var strange, normalIndex int
	strangeIndex = -1
	normal = list[0]
	for i, n := range list[1:] {
		if n == normal {
			continue
		}
		if n == strange {
			normal, strange = strange, normal
			normalIndex, strangeIndex = strangeIndex, normalIndex
			continue
		}
		strange = n
		strangeIndex = i + 1
	}
	return
}

type Program struct {
	Name            string
	Weight          int
	SubProgramNames []string
	SubPrograms     []*Program
	Parent          *Program
}

func creteProgramFromNote(note string) (p *Program) {
	r, _ := regexp.Compile("^([^ ]+) \\(([0-9]+)\\)( -> (.*))?$")
	res := r.FindAllStringSubmatch(note, -1)[0]

	weight, _ := strconv.Atoi(res[2])
	var subs []string
	if res[4] == "" {
		subs = make([]string, 0)
	} else {
		subs = strings.Split(res[4], ", ")
	}
	p = &Program{
		Name:            res[1],
		Weight:          weight,
		SubProgramNames: subs,
	}
	return
}

func (p Program) getTotalWeight() (totalWeight int) {
	totalWeight = p.Weight
	for _, sub := range p.SubPrograms {
		totalWeight += sub.getTotalWeight()
	}
	return
}

func (p Program) normalize(newVal int) int {
	return newVal
}

func (p Program) balance(targetVal int) (newBalance int) {
	fmt.Printf("---\nBalancing %+v\n", p)
	weights := make([]int, len(p.SubPrograms))
	for i, sub := range p.SubPrograms {
		w := sub.getTotalWeight()
		targetVal -= w
		weights[i] = w
	}
	fmt.Printf("Calculated weights: %+v\n", weights)
	strangeIdx, normalVal := whosStrange(weights)
	if strangeIdx >= 0 {
		fmt.Printf("The strange is %+s\n(index %d)\nthe new val should be %d\n",
			p.SubPrograms[strangeIdx].Name,
			strangeIdx,
			normalVal,
		)
		return p.SubPrograms[strangeIdx].balance(normalVal)
	}
	return targetVal
}

func remove(s []string, i int) []string {
	s[len(s)-1], s[i] = s[i], s[len(s)-1]
	return s[:len(s)-1]
}

func main() {

	lines := readFile("input")
	r, _ := regexp.Compile("[a-z]+")
	programMentions := make(map[string]int)
	programs := make(map[string]*Program)
	for _, line := range lines {
		for _, name := range r.FindAllString(line, -1) {
			programMentions[name]++
		}
		p := creteProgramFromNote(line)
		programs[p.Name] = p
	}

	rootProgramName := ""
	for name, mentions := range programMentions {
		if mentions == 1 {
			fmt.Println(name)
			rootProgramName = name
			break
		}
	}

	// set the subprograms
	for _, p := range programs {
		for _, subName := range p.SubProgramNames {
			sub := programs[subName]
			sub.Parent = p
			p.SubPrograms = append(p.SubPrograms, sub)
		}
	}

	fmt.Println(programs[rootProgramName].balance(-1))
}
