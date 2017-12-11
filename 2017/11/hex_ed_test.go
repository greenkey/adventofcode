package main

import (
	"strings"
	"testing"
)

func TestFindPathDistance(t *testing.T) {
	type testCase struct {
		s    string
		dist int
	}
	testcases := []testCase{
		{"n,s", 0},
		{"ne,sw", 0},
		{"nw,se", 0},
		{"ne,s", 1},
		{"ne,nw", 1},
		{"se,n", 1},
		{"se,sw", 1},
		{"s,ne", 1},
		{"s,nw", 1},
		{"sw,n", 1},
		{"sw,se", 1},
		{"nw,s", 1},
		{"nw,ne", 1},
		{"n,sw", 1},
		{"n,we", 1},
		{"ne,ne,ne", 3},
		{"ne,ne,sw,sw", 0},
		{"ne,ne,s,s", 2},
		{"se,sw,se,sw,sw", 3},
	}

	for _, tc := range testcases {
		dist, _ := findPathDistance(strings.Split(tc.s, ","))
		if tc.dist != dist {
			t.Errorf("%s should have distance %d, got %d", tc.s, tc.dist, dist)
		}
	}
}
