#include <bits/stdc++.h>
#define sz(a) (int)a.size()
#define file ""

using namespace std;

const int N = 300003;

/// Move disks from src to dest
struct Move
{
    /// number of disks to move
    int disks;
    /// index of source, destination and auxiliary pegs
    int src, dest, aux;
};

void solve(int n)
{
    stack <Move> st;
    st.push({n, 1, 3, 2});
    while (sz(st))
    {
        auto m = st.top();
        st.pop();
        if (m.disks == 1)
            cout << "Move a disk from peg " << m.src << " to peg " << m.dest << '\n';
        else
        {
            st.push({m.disks - 1, m.aux, m.dest, m.src});
            st.push({1, m.src, m.dest, m.aux});
            st.push({m.disks - 1, m.src, m.aux, m.dest});
        }
    }
}
int main()
{
    int n;
    cout << "Input number of disks: ";
    cin >> n;
    solve(n);
    return 0;
}
