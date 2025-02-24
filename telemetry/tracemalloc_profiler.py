import tracemalloc

#If the system has little free memory, snapshots can be written on disk using the Snapshot.dump() method to analyze the snapshot offline.
#Then use the Snapshot.load() method reload the snapshot.

# list to store memory snapshots
snaps = []


def snapshot():
    snaps.append(tracemalloc.take_snapshot())


def display_stats():
    stats = snaps[0].statistics('filename')
    print("\n*** top 5 stats grouped by filename ***")
    for s in stats[:5]:
        print(s)


def compare():
    first = snaps[0]
    for snapshot in snaps[1:]:
        stats = snapshot.compare_to(first, 'lineno')
        print("\n*** top 10 stats ***")
        for s in stats[:10]:
            print(s)


def print_trace():
    # pick the last saved snapshot, filter noise
    snapshot = snaps[-1].filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<frozen importlib._bootstrap_external>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    largest = snapshot.statistics("traceback")[0]

    print(f"\n*** Trace for largest memory block - ({largest.count} blocks, {largest.size / 1024} Kb) ***")
    for l in largest.traceback.format():
        print(l)

    print("######################################################################################")

    for st in snapshot.statistics("traceback"):

        print(f"\n*** Trace for current memory block - ({st.count} blocks, {st.size / 1024} Kb) ***")
        for l in st.traceback.format():
            print(l)