b=tuple
I=range
M=None
D=abs
import json as A,os,urllib.request
O=[0,100,320,330,500,900,0]
a='HHHHHHHHRRRRRRRRJJLNNLJJIIJMMJIIHHHLLHHHIGFHHFGIIJJDDJJIHHHHHHHH>@BBBB@>@DHHHHD@BHJKKJHBBIKLLKIBBHKLLKHBBIJKKJIB@DHIIHD@>@BBBB@>'
N=[[(ord(A)-72)*5 for A in a[A*64:A*64+64]]for A in I(2)]
N[2:2]=[[0]*64]*4
E=-17,-15,15,17
B=-16,-1,1,16
S=-33,-31,-18,-14,14,18,31,33
C=E+B
c={2:S,3:E,4:B,5:C,6:C}
T=[A for A in I(128)if not A&136]
J=K=10**5
G={}
F=[0]
U={116:12,4:3,119:14,112:13,7:11,0:7}
class V:0
def W(b,sq,by):
	for B in C:
		A=sq+B
		while not A&136 and not b[A]:A+=B
		if not A&136 and(F:=b[A])and(F>0)==(by>0)and D(F)in((3,5)if B in E else(4,5)):return 1
	for(G,H)in((S,2),(C,6),((15,17)if by>0 else(-17,-15),1)):
		for B in G:
			A=sq+B
			if not A&136 and b[A]==H*by:return 1
	return 0
def L(p,sd):return W(p.b,p.k[0]if sd>0 else p.k[1],-sd)
def P(p,cap=0):
	J=cap;D=p.b;C=p.s;P=[];E=P.append
	for A in T:
		K=D[A]
		if not K or(K>0)!=(C>0):continue
		M=K*C
		if M==1:
			F=-16*C;G=A+F
			if not J and not D[G]:
				for N in(5,4,3,2)if G<16 or G>111 else(0,):E((A,G,N))
				if G//16 not in(0,7)and A//16==(6 if C>0 else 1)and not D[A+2*F]:E((A,A+2*F,0))
			for Q in(-1,1):
				B=A+F+Q
				if B&136:continue
				H=D[B]
				if H and(H>0)!=(C>0):
					for N in(5,4,3,2)if B<16 or B>111 else(0,):E((A,B,N))
				elif B==p.e:E((A,B,0))
		else:
			for F in c[M]:
				B=A+F
				while not B&136:
					H=D[B]
					if not H:
						if not J:E((A,B,0))
					else:
						if(H>0)!=(C>0):E((A,B,0))
						break
					if M in(2,6):break
					B+=F
	if not J and not L(p,p.s):
		I=116 if C>0 else 4
		for(R,O)in((1,2),(2,-2))if C>0 else((4,2),(8,-2)):
			if p.c&R and all(not D[I+A]for A in((1,2)if O>0 else(-1,-2,-3)))and all(not W(D,I+A,-C)for A in(0,O//2)):E((I,I+O,0))
	return P
def Q(p,m):
	E,A,H=m;B=V();C=p.b[:];F=p.s;G=C[E];B.b=C;B.s=-F;B.c=p.c;B.e=-1;B.k=p.k[:]
	if G==F and A==p.e:C[A+16*F]=0
	J=H*F if H else G;C[E]=0;C[A]=J
	if D(G)==6:
		B.k[0 if F>0 else 1]=A
		if D(A-E)==2:I,K={118:(119,117),114:(112,115),6:(7,5),2:(0,3)}[A];C[I],C[K]=0,C[I]
	B.c=p.c&U.get(E,15)&U.get(A,15)
	if G==F and D(A-E)==32:B.e=(E+A)//2
	return B
def X(p):
	F=p.b;C=0
	for(E,G)in enumerate(T):
		A=F[G]
		if A:B=D(A);C+=(O[B]+N[B-1][E if A>0 else E^56])*(A//B)
	return C*p.s
def R(p,d,a,be):
	A=be;S=b(p.b),p.s,p.c,p.e;F[0]+=1
	if F[0]>=K:return X(p)
	N=L(p,p.s)
	if d<=0:
		if not N:
			T=X(p)
			if T>=A:return A
			if T>a:a=T
		H=0
		for I in P(p,0 if N else 1):
			C=Q(p,I)
			if L(C,-C.s):continue
			H+=1;E=-R(C,-1,-A,-a)
			if F[0]>=K:return a
			if E>=A:return A
			if E>a:a=E
		if N and not H:return-J
		return a
	B=G.get(S)
	if B and B[0]>=d and(B[3]==0 or B[3]==1 and B[1]>=A or B[3]==2 and B[1]<=a):return B[1]
	V=P(p);V.sort(key=lambda m:-(O[D(p.b[m[1]])]*16-D(p.b[m[0]]))if p.b[m[1]]else-(O[m[2]]*16)if m[2]else 0);H=0;U=M
	for I in V:
		C=Q(p,I)
		if L(C,-C.s):continue
		H+=1;E=-R(C,d-1,-A,-a)
		if F[0]>=K:return a
		if E>=A:G[S]=d,A,I,1;return A
		if E>a:a=E;U=I
	if not H:return-J if N else 0
	G[S]=d,a,U,2 if U is M else 0;return a
def d(fen):
	A=V();A.b=[0]*128;A.c=0;A.e=-1;A.k=[116,4];B=fen.split();D=0
	for C in B[0]:
		if C=='/':D+=8
		elif C.isdigit():D+=int(C)
		else:
			E='PNBRQK'.index(C.upper())+1;F=E if C.isupper()else-E;A.b[D]=F
			if E==6:A.k[0 if F>0 else 1]=D
			D+=1
	A.s=1 if B[1]=='w'else-1
	if B[2]!='-':
		for C in B[2]:A.c|=1<<'KQkq'.index(C)
	if B[3]!='-':A.e=(8-int(B[3][1]))*16+ord(B[3][0])-97
	return A
def Y(m):C,D,A=m;B=lambda x:'abcdefgh'[x%16]+str(8-x//16);return B(C)+B(D)+('nbrq'[A-2]if A else'')
def H(path,body):return A.loads(urllib.request.urlopen(Z+path,A.dumps(body).encode()).read())
def e():
	N='status';C='game';global Z;Z=os.environ['MAKEFUN_ENV_URL']
	while 1:
		A=H('/game',{})
		if A[N]=='done':return
		while A[N]=='your_move':
			B=d(A['start_fen'])
			for O in A['moves']:
				for L in P(B):
					if Y(L)==O:B=Q(B,L);break
			G.clear();F[0]=0;D=M
			for S in I(1,64):
				R(B,S,-J-1,J+1);E=G.get((b(B.b),B.s,B.c,B.e))
				if E and E[2]:D=E[2]
				if F[0]>=K:break
			if D is M:A=H('/resign',{C:A[C]});break
			A=H('/move',{C:A[C],'move':Y(D)})
e()