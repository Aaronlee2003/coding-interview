#include<stdio.h>
#include<stdlib.h>
LinearSearch(int *a, int len, int val) {
    for (int i=0;i<len;i++){
        if(a[i]==val){
            return i;
        }
    }
}