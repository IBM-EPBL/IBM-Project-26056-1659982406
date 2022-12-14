{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "FTE7A-sOr64q"
      },
      "outputs": [],
      "source": [
        "from tensorflow.keras.preprocessing.image import ImageDataGenerator"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "train_datagen = ImageDataGenerator(rescale=1./255,\n",
        "                                   zoom_range=0.2,\n",
        "                                   horizontal_flip=True)"
      ],
      "metadata": {
        "id": "8epn6wrksGvg"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "test_datagen = ImageDataGenerator(rescale=1./255)"
      ],
      "metadata": {
        "id": "EdJNJYJFsMjo"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "xtrain = train_datagen.flow_from_directory('/content//drive/MyDrive/flowers',\n",
        "                                           target_size=(64,64),\n",
        "                                           class_mode='categorical',\n",
        "                                           batch_size=100)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QlVXYwR5sQda",
        "outputId": "8aac08ef-889c-4baa-a50c-d534865770c8"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 4317 images belonging to 5 classes.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "IMAGE AUGMENTATION"
      ],
      "metadata": {
        "id": "nbz4ZjW7ulQ3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from tensorflow.keras.models import Sequential\n",
        "from tensorflow.keras.layers import Convolution2D,MaxPooling2D,Flatten,Dense"
      ],
      "metadata": {
        "id": "uk-UGFvysrna"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "CNN MODEL"
      ],
      "metadata": {
        "id": "jJX_UuwyvAJZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "model = Sequential()\n",
        "model.add(Convolution2D(32,(3,3),activation='relu',input_shape=(64,64,3))) # Convolution layer\n",
        "model.add(MaxPooling2D(pool_size=(2,2))) # Max pooling layer\n",
        "model.add(Flatten()) # Flatten layer\n",
        "# Fully connected layers (ANN)\n",
        "model.add(Dense(300,activation='relu')) # Hidden layer 1\n",
        "model.add(Dense(150,activation='relu')) # Hidden layer 2\n",
        "model.add(Dense(4,activation='softmax')) # Output layer"
      ],
      "metadata": {
        "id": "-LBcIWAWsvhX"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "COMPILE THE MODEL"
      ],
      "metadata": {
        "id": "m1tlC26eu46Y"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])"
      ],
      "metadata": {
        "id": "DpOZAIkJsy3Q"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "SAVE THE MODEL"
      ],
      "metadata": {
        "id": "I8308Zuvu9ZP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "model.save('Flower.h5')"
      ],
      "metadata": {
        "id": "FSgxTAhqtNIX"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "TEST THE MODEL"
      ],
      "metadata": {
        "id": "xlEyckOnvFef"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "from tensorflow.keras.preprocessing import image"
      ],
      "metadata": {
        "id": "f8wbDr-ktexL"
      },
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "img = image.load_img('/content/drive/MyDrive/flowers/dandelion/10043234166_e6dd915111_n.jpg',target_size=(64,64))"
      ],
      "metadata": {
        "id": "IP1YnDHMthh4"
      },
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "img"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 81
        },
        "id": "-jDXjeZWtn0A",
        "outputId": "6987fef7-073b-4535-a49b-1a40a511ef6c"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<PIL.Image.Image image mode=RGB size=64x64 at 0x7FC823134A10>"
            ],
            "image/png": "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\n"
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Converting image to array\n",
        "\n",
        "x = image.img_to_array(img)\n",
        "x"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZQROn0eWtuPv",
        "outputId": "22695a00-7c1c-4916-9667-b98aab50ed34"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[[ 3.,  6.,  0.],\n",
              "        [ 8.,  9.,  1.],\n",
              "        [ 7.,  8.,  0.],\n",
              "        ...,\n",
              "        [35., 44.,  1.],\n",
              "        [35., 44.,  1.],\n",
              "        [35., 43.,  2.]],\n",
              "\n",
              "       [[ 5.,  8.,  1.],\n",
              "        [ 6.,  7.,  0.],\n",
              "        [ 6.,  7.,  1.],\n",
              "        ...,\n",
              "        [30., 36.,  0.],\n",
              "        [30., 38.,  0.],\n",
              "        [31., 39.,  0.]],\n",
              "\n",
              "       [[ 7.,  8.,  2.],\n",
              "        [ 7.,  8.,  2.],\n",
              "        [ 5.,  8.,  0.],\n",
              "        ...,\n",
              "        [19., 22.,  1.],\n",
              "        [19., 24.,  1.],\n",
              "        [23., 29.,  3.]],\n",
              "\n",
              "       ...,\n",
              "\n",
              "       [[17., 20.,  1.],\n",
              "        [23., 27.,  2.],\n",
              "        [24., 30.,  2.],\n",
              "        ...,\n",
              "        [23., 27.,  0.],\n",
              "        [23., 29.,  1.],\n",
              "        [21., 27.,  1.]],\n",
              "\n",
              "       [[16., 19.,  0.],\n",
              "        [23., 28.,  0.],\n",
              "        [26., 31.,  1.],\n",
              "        ...,\n",
              "        [19., 23.,  0.],\n",
              "        [25., 27.,  5.],\n",
              "        [19., 24.,  1.]],\n",
              "\n",
              "       [[17., 20.,  1.],\n",
              "        [22., 26.,  0.],\n",
              "        [26., 31.,  1.],\n",
              "        ...,\n",
              "        [18., 21.,  0.],\n",
              "        [20., 24.,  1.],\n",
              "        [21., 25.,  2.]]], dtype=float32)"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Expanding dimensions\n",
        "\n",
        "x = np.expand_dims(x,axis=0)\n",
        "x"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "knGc0Z99tyH_",
        "outputId": "76bcfe1e-be3d-4613-e804-f5367f010b90"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[[[ 3.,  6.,  0.],\n",
              "         [ 8.,  9.,  1.],\n",
              "         [ 7.,  8.,  0.],\n",
              "         ...,\n",
              "         [35., 44.,  1.],\n",
              "         [35., 44.,  1.],\n",
              "         [35., 43.,  2.]],\n",
              "\n",
              "        [[ 5.,  8.,  1.],\n",
              "         [ 6.,  7.,  0.],\n",
              "         [ 6.,  7.,  1.],\n",
              "         ...,\n",
              "         [30., 36.,  0.],\n",
              "         [30., 38.,  0.],\n",
              "         [31., 39.,  0.]],\n",
              "\n",
              "        [[ 7.,  8.,  2.],\n",
              "         [ 7.,  8.,  2.],\n",
              "         [ 5.,  8.,  0.],\n",
              "         ...,\n",
              "         [19., 22.,  1.],\n",
              "         [19., 24.,  1.],\n",
              "         [23., 29.,  3.]],\n",
              "\n",
              "        ...,\n",
              "\n",
              "        [[17., 20.,  1.],\n",
              "         [23., 27.,  2.],\n",
              "         [24., 30.,  2.],\n",
              "         ...,\n",
              "         [23., 27.,  0.],\n",
              "         [23., 29.,  1.],\n",
              "         [21., 27.,  1.]],\n",
              "\n",
              "        [[16., 19.,  0.],\n",
              "         [23., 28.,  0.],\n",
              "         [26., 31.,  1.],\n",
              "         ...,\n",
              "         [19., 23.,  0.],\n",
              "         [25., 27.,  5.],\n",
              "         [19., 24.,  1.]],\n",
              "\n",
              "        [[17., 20.,  1.],\n",
              "         [22., 26.,  0.],\n",
              "         [26., 31.,  1.],\n",
              "         ...,\n",
              "         [18., 21.,  0.],\n",
              "         [20., 24.,  1.],\n",
              "         [21., 25.,  2.]]]], dtype=float32)"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model.predict(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FuKiB9vht1EX",
        "outputId": "9d4d156b-f9c0-41f8-ba9d-e7cdfc45e49d"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[8.1779763e-02, 9.1822016e-01, 2.1105427e-24, 1.6366634e-27]],\n",
              "      dtype=float32)"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "op = ['daisy','dandelion','rose','sunflower','tulip']\n",
        "pred = np.argmax(model.predict(x))\n",
        "op[pred]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "j3gbpKghuLMn",
        "outputId": "25028b1a-439c-4986-e99f-e18bc5583c3d"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'dandelion'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Testing\n",
        "\n",
        "img = image.load_img('/content/drive/MyDrive/flowers/daisy/1031799732_e7f4008c03.jpg',target_size=(64,64))\n",
        "x = image.img_to_array(img)\n",
        "x = np.expand_dims(x,axis=0)\n",
        "pred = np.argmax(model.predict(x))\n",
        "op[pred]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "JHoB5Iqjt9Ef",
        "outputId": "ebbffb2f-aece-43e0-d7b0-080bc000a0dc"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'dandelion'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 26
        }
      ]
    }
  ]
}