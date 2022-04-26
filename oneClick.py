import step1
import step2
import step3
import personal_keys

if __name__ == '__main__':
    step1.save_from_clipboard()
    step1.pre_processing()
    step2.get_address_coord(method='amap', key=personal_keys.amap_key)
    step3.final_processing()
