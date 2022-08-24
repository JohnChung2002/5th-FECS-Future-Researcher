import os

GDRIVE = { 1 :{'call_center.dat': '1o0oNlvlvsCgPcuqTmCU7faIgLpsVY7nl', 'catalog_page.dat': '1dVrGnE6q-qp17G000Zk0FfxyRf2vlthx', 'catalog_returns.dat': '1myzozv3m-K5QOa3rbU2dP2vfbYOg4On2', 'catalog_sales.dat': '1gTM1FScdjLDZkemxZYcYNQGI2IVRc3cJ', 'customer_address.dat': '11q-rlJBLlr0NEc0-KSO5CDqXls_gU0k0', 'customer_demographics.dat': '1bq3iMLb5yqa8Dbp7EiLAcsrOkYchSr4e', 'customer.dat': '1-2rh_dnjGkkEiD2PvoNI5QxiI-c_eKdV', 'date_dim.dat': '1NjSE2hvWcIhcTTHgg4NlzOvNslJ06A1f', 'dbgen_version.dat': '1HXZR3VOWuBQn30Yw7rXVuII_cSlsxLnG', 'household_demographics.dat': '1O35AhyKhUh0hhrDt1MVq4gmD_YSU7EMl', 'income_band.dat': '1gqPh_WSlCcvbfZvtzvPszfCTnLS6CywB', 'inventory.dat': '1b2lHBBu4KQTZeD6Nx_SGg1AkDc-t1EZi', 'item.dat': '1u3nLGHkAas3WZIjQSTJ_awUA1eYOScjF', 'promotion.dat': '10a0XBvutjk5lmHULEVuG1fhvy8R572tr', 'reason.dat': '1GCLzmCRH1prhpiaS6U8vQ4whofyVgN84', 'ship_mode.dat': '1rqQn2Dqxje1h5V0SiSU7193aBQluGK8p', 'store_returns.dat': '16opN0JaGXpMXqqhbD7OMv8AtlM_DDZoO', 'store_sales.dat': '1uyARB4KfJEfuA6gfIIQnQjYOWfhajR_D', 'store.dat': '1YHk3j5uukxE9IAc1AkQVFqUHUO9pEmOz', 'time_dim.dat': '1tHmpkxePc2PoFO6lNttMkYi12R0V3aKk', 'warehouse.dat': '1qPVQQaPRGfjEGuBg2ZgTWk0Ftf-78AVA', 'web_page.dat': '11tZVydxyWEpNQplLKytBSYdLNP01e2EX', 'web_returns.dat': '1vGpY5mBflwq04CoscBsuczsvF-7doNXh', 'web_sales.dat': '1JXmqr1jnlSfDT6jQsW35xRFszct77vUH', 'web_site.dat': '1MVyhvYcbpe4rNZ9LR-rnteaumh78BXJp'},
2: {'call_center.dat': '1zQNccQxILfEj4KAVx4R6Ah9THw2YVzL1', 'catalog_page.dat': '1-6NmeRK9KvVf4i1N3qQqX0TKOylnOH-b', 'catalog_returns.dat': '1PGDETEei1DIsrDiGkx4h_HiAsNVfaqSN', 'catalog_sales.dat': '14SE69YstdCJBRixdgrsR-jPJZUzZLSbD', 'customer_address.dat': '14QGexftaeDXmxJrr3zK04PKj_363zTCe', 'customer_demographics.dat': '1--VkNz1Ls4bpyUlxkSVkp8b7kv_XkVSB', 'customer.dat': '14Wm0ruauQBgZ9TwXVFU5f2IbAk1oXzHz', 'date_dim.dat': '1U981sjAKKeP5znsgOnIE-2cbJJ9fbqpE', 'dbgen_version.dat': '1ctkil7AbpHMKzfQRc62tdd9mXGlnCQ7m', 'household_demographics.dat': '1XMLmWYwnUEUZ9PTnvqSwSYsGqY0mxCyn', 'income_band.dat': '1PranduczDUTv80gQWe4mR2P6W3BUzHQ1', 'inventory.dat': '1iBJSRu878Uev7ZWzmmneSJaxuIPnXmoH', 'item.dat': '1YJXTd_INiGjMLTd_nJta5M1HwYUR_ICS', 'promotion.dat': '1qjAT9nlf6fxWZvj1d9N1dmc9RbzG2ikv', 'reason.dat': '1orDoTjSY8ntsxPDHw-Gn99jaFWq7J65Z', 'ship_mode.dat': '1wodnYh8s8pm0aDr18wFjT5rQ59dWnwaS', 'store_returns.dat': '1KLrj8Y8qpx0Xd5M01zDJZVK4QvAAWlFi', 'store_sales.dat': '1pCDwZy-PyPk9yOzdMZjdIGXSSTQkRYKm', 'store.dat': '10xlOZjzIFdI6huWpKBsURyaLfxTKZWYB', 'time_dim.dat': '1lgI2Hy2aK_p3uW7xG5zRPqBbwP7yl7C9', 'warehouse.dat': '1dStzsZj19X3cUTj9an-GvoTxagrDEdxL', 'web_page.dat': '1C5nCbVpUvekwtS1Ruai2BA_1jZKaCT-i', 'web_returns.dat': '1hyCd_GE7CTVKsfHAFzKBzGHdy63q9LIp', 'web_sales.dat': '1Gda2AAV_OPaBARQucLQWuTKEBefCVmgX', 'web_site.dat': '1bkMsRqna6yT7aUqttBw0LB-wLJFK9nf_'}}

DPATH = {1: "/tmp", 2: "/var/lib/mysql-files"}

def menu(num, option):
    for key in option:
        print(f"{key}. {option[key][num]}")
    choice = int(input("Select an option: "))
    if choice in option.keys():
        return choice
    return False

def download(choice1, choice2):
    for filename in GDRIVE[choice1]:
        os.system(f"curl -b 'cookies.txt' -L 'https://drive.google.com/uc?id={GDRIVE[choice1][filename]}&export=download&confirm=yes' -o {DPATH[choice2]}/{filename}")

if __name__ == "__main__":
    option = {1 : ["30GB", "Normal"], 2 : ["100GB", "MySQL"]}
    choice = [0,0]
    for i in range(2):
        choice[i] = menu(i, option)
        if choice[i] not in option.keys():
            break
    if (choice[0] in option.keys() and choice[1] in option.keys()):
        download(choice[0], choice[1])
    else:
        print("Invalid selection. Exiting...")