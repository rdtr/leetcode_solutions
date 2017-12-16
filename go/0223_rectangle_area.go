func computeArea(A int, B int, C int, D int, E int, F int, G int, H int) int {
	var X, Y, Z, W int // intersection

	if A > E {
		A, B, C, D, E, F, G, H = E, F, G, H, A, B, C, D
	}

	if C <= E {
		return abs(C-A)*abs(D-B) + abs(G-E)*abs(H-F)
	}

	X = E
	if C <= G {
		Z = C
	} else {
		Z = G
	}

	if B > F {
		A, B, C, D, E, F, G, H = E, F, G, H, A, B, C, D
	}

	if D <= F {
		return abs(C-A)*abs(D-B) + abs(G-E)*abs(H-F)
	}

	Y = F
	if D <= H {
		W = D
	} else {
		W = H
	}

	return abs(C-A)*abs(D-B) + abs(G-E)*abs(H-F) - abs(Z-X)*abs(W-Y)
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}