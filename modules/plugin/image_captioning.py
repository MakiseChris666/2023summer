from transformers import GPT2TokenizerFast, ViTImageProcessor, VisionEncoderDecoderModel
from PIL import Image

import warnings
warnings.filterwarnings('ignore')

model_raw = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
image_processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = GPT2TokenizerFast.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

curImagePath = ''

def caption(filepath, greedy = True, model = model_raw):
    image = Image.open(filepath)
    pixel_values = image_processor(image, return_tensors ="pt").pixel_values
    # plt.imshow(np.asarray(image))
    # plt.show()

    if greedy:
        generated_ids  = model.generate(pixel_values, max_new_tokens = 30)
    else:
        generated_ids  = model.generate(
            pixel_values,
            do_sample=True,
            max_new_tokens = 30,
            top_k=2)
    generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return generated_text

def imageQuery(msg):
    imgInfo = caption(curImagePath)
    return imgInfo + '\n以上是对一张图片的英文描述，请你根据这段描述不加修饰地用中文回答以下问题，你的回答只能包含描述中的信息：\n' + msg

if __name__ == '__main__':
    print(caption(r'D:\ImageStitchingWorkplace\2023summer\external\000000039769.jpg'))