df = pd.read_csv('/Users/user/my_file.txt', skiprows = 2, header = None, delimiter = "\t")
df.head()

#   0 1
#	0	-0.329438	-53.874714
#	1	-0.361870	-53.647690
#	2	-0.361870	-53.744986
#	3	-0.361870	-53.874714
#	4	-0.361870	-53.680122

len(df)
# Out: 12101700

%timeit df[1].plot()
# Out: 1 loops, best of 3: 1min 18s per loop
