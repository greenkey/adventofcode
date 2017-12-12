package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"sort"
	"strconv"
)

type set []int

func (s set) Len() int           { return len(s) }
func (s set) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }
func (s set) Less(i, j int) bool { return s[i] < s[j] }
func removeDuplicates(s set) (new set) {
	prev := -1
	sort.Sort(s)
	for _, n := range s {
		if n != prev {
			new = append(new, n)
			prev = n
		}
	}
	return
}

func main() {

	scanner := bufio.NewScanner(os.Stdin)

	r, _ := regexp.Compile("([0-9]+)")
	cityMap := make(map[int]*set)

	for scanner.Scan() {
		line := scanner.Text()
		res := r.FindAllStringSubmatch(line, -1)
		group := make(set, len(res))
		for i, r := range res {
			group[i], _ = strconv.Atoi(r[0])
		}
		group = removeDuplicates(group)
		for _, n := range group {
			g, ok := cityMap[n]
			if ok {
				group = removeDuplicates(append(*g, group...))
			}
		}
		for _, n := range group {
			cityMap[n] = &group
		}

	}
	fmt.Println(len(*cityMap[0]))

	uniqueItems := make([]*set, 0)
	for _, item := range cityMap {
		found := false
		for _, uniqueItem := range uniqueItems {
			if uniqueItem == item {
				found = true
				break
			}
		}
		if !found {
			uniqueItems = append(uniqueItems, item)
		}
	}
	fmt.Println(len(uniqueItems))

}
