class ProductOfNumbers {
private:
vector<int> prefix_product;
int length;

public:
    ProductOfNumbers() {
        prefix_product.push_back(1);
        length = 1;
    }
    
    void add(int num) {
        if (num == 0) {
            prefix_product = {1};
            length = 1;
            return;
        }
            
        prefix_product.push_back(prefix_product.back() * num);
        ++length;
    }
    
    int getProduct(int k) {
        return length <= k ? 0 : prefix_product.back() / prefix_product[length-k-1];
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */
 