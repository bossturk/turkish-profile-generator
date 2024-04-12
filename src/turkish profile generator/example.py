from UserProfileGenerator import UserProfileGenerator


# Kullanım örneği
generator = UserProfileGenerator(12, 15,"Female")
# profile1 = generator.reset('Female')  # 'Female' cinsiyeti verildiğinde
profile2 = generator.reset()          # Hiçbir cinsiyet verilmediğinde, önceki cinsiyete göre devam eder

print("\nGenerated Profile 2:")
print(profile2)