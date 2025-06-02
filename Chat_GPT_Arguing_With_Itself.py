from ai import call_gpt

def main():
    topic = input("What is your topic? ")
    question = call_gpt(f"Ask a question about {topic} that can be answered in one sentence.")
    print(question)
    answer = call_gpt(f"Answer the following question with one sentence.  {question}")
    print(answer)
    print("SERIOUS VERSION")
    argument1 = call_gpt(f"Make an argument in one sentence why the following sentence is wrong.  {answer}")
    print(argument1)
    for i in range(15):
        argument2 = call_gpt(f"Make an argument in one sentence why the following sentence is wrong.  {argument1}")
        print(argument2)
        argument1 = call_gpt(f"Make an argument in one sentence why the following sentence is wrong.  {argument2}")
        print(argument1)
    print("FUN VERSION")
    argument1 = call_gpt(f"Make a ridiculous argument in one sentence why the following sentence is wrong.  {answer}")
    print(argument1)
    for i in range(15):
        argument2 = call_gpt(f"Make a ridiculous argument in one sentence why the following sentence is wrong.  {argument1}")
        print(argument2)
        argument1 = call_gpt(f"Make a ridiculous argument in one sentence why the following sentence is wrong.  {argument2}")
        print(argument1)


if __name__ == "__main__":
    main()
