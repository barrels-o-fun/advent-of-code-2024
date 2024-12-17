// Part 1 Total:  432
// Part 2 Total:  0

// real    0m0.139s
// user    0m0.152s
// sys     0m0.006s

package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

// 31 34 32 30 28 27 24 22
func check_report(report string, acceptError int) bool {
	nums := strings.Split(report, " ")
	var curNum int
	var prevNum int
	errors := 0
	direction := "None"
	for i := range nums {
		foundError := false
		curNum, _ = strconv.Atoi(string(nums[i]))
		if prevNum != 0 {
			absDiff := math.Abs(float64(curNum - prevNum))
			diff := int(curNum - prevNum)
			if absDiff < 1 || absDiff > 3 {
				foundError = true
				errors += 1
			} else if diff > 0 {
				if direction == "dsc" {
					foundError = true
					errors += 1
				} else {
					direction = "asc"
				}
			} else if diff < 0 {
				if direction == "asc" {
					foundError = true
					errors += 1
				} else {
					direction = "dsc"
				}
			}
		}
		if errors > acceptError {

			return false
		}
		if !foundError {
			prevNum = curNum
		}
	}
	return true
}

func main() {
	// part1_total := 0
	part2_total := 0

	// reports := "sampleData.txt"
	reports := "day2.txt"
	f, err := os.Open(reports)
	check(err)

	scanner := bufio.NewScanner(f)

	// var safe_reports []string
	safe_reports_count := 0
	unsafe_reports_count := 0

	for scanner.Scan() {
		report := scanner.Text()
		safe := check_report(report, 0)

		if safe == true {
			// safe_reports = append(safe_reports, line, ":")
			safe_reports_count += 1
			part2_total += 1
			continue
		}

		safe = check_report(report, 1)
		if safe == true {
			part2_total += 1
			continue
		}

		// We also need to check if we can do the report with the first num missing
		var foundIdx int
		for i := range report {
			if report[i] == ' ' {
				foundIdx = i
				break
			}
		}
		newReport := report[foundIdx+1:]
		safe = check_report(newReport, 0)

		if safe == true {
			part2_total += 1
			continue
		} else {
			unsafe_reports_count += 1
		}

	}
	println("Part 1 Total: ", safe_reports_count)
	println("Part 2 Total: ", part2_total, " unsafe reports: ", unsafe_reports_count)
}
