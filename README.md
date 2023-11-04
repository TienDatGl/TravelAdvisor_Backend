# TravelAdvisor_Backend
# I. Config database to Django
  ## 1. Install MySQL Workbench
  ## 2. Create MYSQL Connections:
     - Connection name: root
     - Password: 123456
  ## 3. Open MySQL workbrench
     - Select Administration
     - Data Import/Restore
     - Import from Dump Project Folder 
     - Default Target Schema: tabdb
     - Select tadb and Start Import
  ### ![database config](https://github.com/TienDatGl/TravelAdvisor_Backend/assets/88433859/faf3b9e3-47c4-43b7-a032-1f94d9c963a5)

# II. Config Django
  ## 1. settings.py
  ## 2. scroll down to CORS_ALLOWED_ORIGINS and change 3001 into 3000
  ### 3. ![image](https://github.com/TienDatGl/TravelAdvisor_Backend/assets/88433859/fbd32533-1090-45fa-8d34-676a4de06f9b)

  ## 4. Select Python Interpreter: Crtl + Shift + P
  ## 5. Select
  ### 6. ![image](https://github.com/TienDatGl/TravelAdvisor_Backend/assets/88433859/02b9c2f5-d680-4f1d-b64d-44350f1878fb)
  ## 7. Terminal: py.exe maanage.py runserver


