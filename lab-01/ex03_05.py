def dem_so_lan_xuat_hien(lst):

 count_dict = {}
 for item in lst :
     count_dict[item] +=1
 else:
      count_dict[item] = 1
    
 return count_dict

# Nhập chuỗi từ người dùng

input_string = input("Nhập chuỗi: ")

# Đếm số lần xuất hiện và in kết quả

word_counts = dem_so_lan_xuat_hien(input_string)

for word, count in word_counts.items():
 print(f"{word}: {count}")