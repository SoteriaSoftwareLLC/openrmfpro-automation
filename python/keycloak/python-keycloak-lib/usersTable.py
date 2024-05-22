from prettytable import PrettyTable

myTable = PrettyTable(["User ID", "Username", "Email", "First Name", "Last Name"])

#Add rows
myTable.add_row(["89262f05-8c8b-4bfc-bd4c-e05b153c5773", " dale.bingham@soteriasoft.com", "dale.bingham@soteriasoft.com", "Dale", "Bingham"])
myTable.add_row(["a3e12e0a-6cc5-4b4f-a04e-a124e8a078d3", "dgould", "david.gould@soteriaosft.com", "David", "Gould"])
myTable.add_row(["c023066b-dc9e-4563-9598-02fe377dcd9f", "dtest", " dtest@gmail.com", "D", "Tester"])
myTable.add_row(["becbfe32-6351-412a-90eb-a8b62bbe6867", "openrmfproadmin", "support@soteriasoft.com", "Test", "Administrator"])
myTable.add_row(["63d16c14-773d-4666-90c4-c9e1dfe8db59", "rsmith", "rmsimth@test.com", "Richard", "Smith"])
myTable.add_row(["7d2c8719-c3a3-4d66-b7d4-02b9da9fcda2", "svcsoteriasoft", "svcsoteriasoft@soteriasoft.com", "Soteria Software", "Service Account"])

print(myTable)