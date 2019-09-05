import (
    "strings"
)

func solution(n int) string {
    Pattern := [2]string{"수", "박"}
    var result strings.Builder
    
    for i, _ := range make([]int, n) {
        result.WriteString(Pattern[i % len(Pattern)])
    }
    
    return  result.String()
}