package main

import (
	"testing"
)

func TestGetStreamScore(t *testing.T) {
	type testCase struct {
		s     string
		score int
	}
	testcases := []testCase{
		{"{}", 1},
		{"{{{}}}", 6},
		{"{{},{}}", 5},
		{"{{{},{},{{}}}}", 16},
		{"{<a>,<a>,<a>,<a>}", 1},
		{"{{<ab>},{<ab>},{<ab>},{<ab>}}", 9},
		{"{{<!!>},{<!!>},{<!!>},{<!!>}}", 9},
		{"{{<a!>},{<a!>},{<a!>},{<ab>}}", 3},
		{"{<<<<>}", 1},
		{"{<<<<}{>}", 1},
	}

	for _, tc := range testcases {
		s := getStreamScore(tc.s)
		if tc.score != s {
			t.Errorf("%s should have score %d, got %d", tc.s, tc.score, s)
		}
	}
}
