package main

type ProductOfNumbers struct {
	prefix_product []int
	length         int
}

func Constructor() ProductOfNumbers {
	return ProductOfNumbers{
		prefix_product: []int{1},
		length:         1,
	}
}

func (this *ProductOfNumbers) Add(num int) {
	if num == 0 {
		this.prefix_product = []int{1}
		this.length = 1
		return
	}

	this.prefix_product = append(this.prefix_product, this.prefix_product[this.length-1]*num)
	this.length++
}

func (this *ProductOfNumbers) GetProduct(k int) int {
	if this.length <= k {
		return 0
	}

	return this.prefix_product[this.length-1] / this.prefix_product[this.length-k-1]
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(num);
 * param_2 := obj.GetProduct(k);
 */
