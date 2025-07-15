import csv
import math
import os

def load_points(filename):
    """
    Load 3-D points from columns 6,7,8 (0-based indexing) of a CSV.
    Returns a list of (x,y,z) tuples.
    """
    pts = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                x, y, z = float(row[6]), float(row[7]), float(row[8])
                pts.append((x, y, z))
            except (IndexError, ValueError):
                # skip header or malformed lines
                continue
    return pts

def find_hits(file1, file2, xy_tol=0.25):
    pts1 = load_points(file1)
    pts2 = load_points(file2)
    hits = []

    for x1, y1, z1 in pts1:
        for x2, y2, z2 in pts2:
            dx = x2 - x1
            dy = y2 - y1
            dz = z2 - z1
            denom = dx*dx + dy*dy
            if denom == 0:
                # line is vertical in XY; skip or handle separately
                continue
            # parameter for closest approach in XY to (0,0)
            t0 = -(x1*dx + y1*dy) / denom
            if t0 <= 1:
                # does not extend past P2
                continue

            # coordinates at t0
            xi = x1 + t0*dx
            yi = y1 + t0*dy
            zi = z1 + t0*dz

            if abs(xi) <= xy_tol and abs(yi) <= xy_tol:
                hits.append((x1, y1, z1, x2, y2, z2, xi, yi, zi))

    return hits

def write_hits(hits, out_file='hits.csv'):
    with open(out_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['x1','y1','z1','x2','y2','z2','xi','yi','zi'])
        writer.writerows(hits)


hits = find_hits("clusters\cluster_7.csv", "clusters\cluster_5.csv", xy_tol=0.1)
write_hits(hits, 'hits.csv')
print(f"Found {len(hits)} hitting lines; results in hits.csv")
