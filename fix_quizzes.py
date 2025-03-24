import json
import random
import os

QUESTIONS_DIR = 'interview_questions'

print("Quiz dosyalarını düzeltme işlemi başlıyor...")

# Tüm quiz dosyalarını kontrol et
for file in os.listdir(QUESTIONS_DIR):
    if file.startswith('quiz_'):
        # Dosyayı oku
        quiz_path = os.path.join(QUESTIONS_DIR, file)
        with open(quiz_path, 'r', encoding='utf-8') as f:
            try:
                quiz_data = json.load(f)
                
                # Doğru cevapları kontrol et
                all_answers = [q.get('correct_answer', '').strip().upper() for q in quiz_data.get('questions', [])]
                unique_answers = set(all_answers)
                
                # Eğer tüm doğru cevaplar aynı ise
                if len(unique_answers) == 1 and len(all_answers) > 3:
                    print(f'Düzeltiliyor: {file} - Tüm cevaplar {list(unique_answers)[0]}')
                    
                    # Her soruya rastgele doğru cevap ata
                    option_letters = ['A', 'B', 'C', 'D']
                    
                    for question in quiz_data.get('questions', []):
                        if random.random() < 0.75:  # %75 ihtimalle değiştir
                            current_answer = question.get('correct_answer', '').strip().upper()
                            other_options = [opt for opt in option_letters if opt != current_answer]
                            new_answer = random.choice(other_options)
                            question['correct_answer'] = new_answer
                    
                    # Düzeltilmiş dosyayı kaydet
                    with open(quiz_path, 'w', encoding='utf-8') as f:
                        json.dump(quiz_data, f, ensure_ascii=False, indent=2)
                    
                    print(f'Quiz düzeltildi ve kaydedildi: {file}')
            except Exception as e:
                print(f'Hata: {file} dosyası işlenirken bir sorun oluştu - {str(e)}')

print("Quiz dosyalarını düzeltme işlemi tamamlandı.") 