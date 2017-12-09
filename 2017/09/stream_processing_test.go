package main

import (
	"testing"
)

func TestGetStreamScore(t *testing.T) {
	type testCase struct {
		s       string
		score   int
		removed int
	}
	testcases := []testCase{
		{"{}", 1, 0},
		{"{{{}}}", 6, 0},
		{"{{},{}}", 5, 0},
		{"{{{},{},{{}}}}", 16, 0},
		{"{<a>,<a>,<a>,<a>}", 1, 4},
		{"{{<ab>},{<ab>},{<ab>},{<ab>}}", 9, 8},
		{"{{<!!>},{<!!>},{<!!>},{<!!>}}", 9, 0},
		{"{{<a!>},{<a!>},{<a!>},{<ab>}}", 3, 17},
		{"{<<<<>}", 1, 3},
		{"{<<<<}{>}", 1, 5},
	}

	for _, tc := range testcases {
		s, r := getStreamScore(tc.s)
		if tc.score != s {
			t.Errorf("%s should have score %d, got %d", tc.s, tc.score, s)
		}
		if tc.removed != r {
			t.Errorf("%s should have removed %d, got %d", tc.s, tc.removed, r)
		}
	}
}
