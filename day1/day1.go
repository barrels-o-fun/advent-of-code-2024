// $ time ./day1
// Part 1 Total:  1388114

// real    0m0.004s
// user    0m0.004s
// sys     0m0.001s

package main

import (
	"bufio"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	// inFile := "sampleData.txt"
	inFile := "day1.txt"
	f, err := os.Open(inFile)
	check(err)

	scanner := bufio.NewScanner(f)

	var input []string
	for scanner.Scan() {
		line := scanner.Text()
		input = append(input, line)
	}

	var lhs []string
	var rhs []string
	var diff []float64

	for i := range input {
		line := input[i]
		nums := strings.Split(line, "   ")
		lhs = append(lhs, nums[0])
		rhs = append(rhs, nums[1])
	}

	sort.Strings(lhs)
	sort.Strings(rhs)

	part1_total := 0

	for i := 0; i < len(lhs); i++ {
		num1, _ := strconv.Atoi(lhs[i])
		num2, _ := strconv.Atoi(rhs[i])
		res := num1 - num2
		fres := float64(res)
		abs := math.Abs(fres)
		diff = append(diff, abs)
		part1_total += int(abs)
	}

	// fmt.Println(lhs)
	// fmt.Println(rhs)
	// fmt.Println(diff)
	println("Part 1 Total: ", part1_total)
}
