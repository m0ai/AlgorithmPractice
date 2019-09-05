func solution(s string) string {
    mid := int(float64(len(s) / 2 + 1))
    return s[mid-0.5:mid+1]
}