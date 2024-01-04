from transformers import CLIPTextModel, CLIPTokenizer
import pandas as pd

tk  =CLIPTokenizer.from_pretrained("models/StableDiffusion", subfolder="tokenizer")

df = pd.read_csv('/home/ubuntu/animated_diff_ds.csv')


df['name_token_len'] = df['name'].apply(lambda x: len(tk(x).input_ids) if isinstance(x, str) else 0)

print(df['name_token_len'] )

print(f"max len: {df['name_token_len'].max()}")