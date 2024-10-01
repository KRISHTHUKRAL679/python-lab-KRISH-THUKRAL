nums = (1, 2, 3, 4, 5, 6, 7)
print("Original list: ", nums)
result = map(lambda x: x + x + x, nums)
print("\nTriple of said list numbers:")
print(list(result))

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Employee {
    int SSN;
    char Name[50];
    char Dept[50];
    char Designation[50];
    float Sal;
    char PhNo[20];
    struct Employee* next;
    struct Employee* prev;
} Employee;

Employee* createNode(int SSN, char* Name, char* Dept, char* Designation, float Sal, char* PhNo) {
    Employee* newNode = (Employee*)malloc(sizeof(Employee));
    newNode->SSN = SSN;
    strcpy(newNode->Name, Name);
    strcpy(newNode->Dept, Dept);
    strcpy(newNode->Designation, Designation);
    newNode->Sal = Sal;
    strcpy(newNode->PhNo, PhNo);
    newNode->next = newNode->prev = NULL;
    return newNode;
}

void insertAtEnd(Employee** head, Employee* newNode) {
    if (*head == NULL) {
        *head = newNode;
    } else {
        Employee* temp = *head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->prev = temp;
    }
}

void displayDLL(Employee* head) {
    int count = 0;
    while (head != NULL) {
        printf("SSN: %d, Name: %s, Dept: %s, Designation: %s, Sal: %.2f, PhNo: %s\n",
               head->SSN, head->Name, head->Dept, head->Designation, head->Sal, head->PhNo);
        head = head->next;
        count++;
    }
    printf("Number of nodes: %d\n", count);
}

void insertAtFront(Employee** head, Employee* newNode) {
    if (*head == NULL) {
        *head = newNode;
    } else {
        newNode->next = *head;
        (*head)->prev = newNode;
        *head = newNode;
    }
}

void deleteAtEnd(Employee** head) {
    if (*head == NULL) {
        printf("DLL is empty\n");
    } else {
        Employee* temp = *head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        if (temp->prev) {
            temp->prev->next = NULL;
        } else {
            *head = NULL; // List becomes empty
        }
        free(temp);
    }
}

void deleteAtFront(Employee** head) {
    if (*head == NULL) {
        printf("DLL is empty\n");
    } else {
        Employee* temp = *head;
        *head = (*head)->next;
        if (*head) {
            (*head)->prev = NULL;
        }
        free(temp);
    }
}

void demoDEQueue(Employee* head) {
    printf("DLL as a Double Ended Queue:\n");
    displayDLL(head);
}

int main() {
    Employee* head = NULL;
    int choice, N;
    printf("Enter the number of employees: ");
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        int SSN;
        char Name[50], Dept[50], Designation[50], PhNo[20];
        float Sal;
        printf("Enter employee %d details:\n", i + 1);
        printf("SSN: ");
        scanf("%d", &SSN);
        printf("Name: ");
        scanf("%s", Name);
        printf("Dept: ");
        scanf("%s", Dept);
        printf("Designation: ");
        scanf("%s", Designation);
        printf("Sal: ");
        scanf("%f", &Sal);
        printf("PhNo: ");
        scanf("%s", PhNo);
        Employee* newNode = createNode(SSN, Name, Dept, Designation, Sal, PhNo);
        insertAtEnd(&head, newNode);
    }

    // Menu for operations
    while (1) {
        printf("\nMenu:\n");
        printf("1. Insert at End\n");
        printf("2. Display DLL\n");
        printf("3. Delete at End\n");
        printf("4. Insert at Front\n");
        printf("5. Delete at Front\n");
        printf("6. Demonstrate as Double Ended Queue\n");
        printf("7. Exit\n");
        printf("Choose an option: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: {
                int SSN;
                char Name[50], Dept[50], Designation[50], PhNo[20];
                float Sal;
                printf("Enter details for new employee:\n");
                printf("SSN: ");
                scanf("%d", &SSN);
                printf("Name: ");
                scanf("%s", Name);
                printf("Dept: ");
                scanf("%s", Dept);
                printf("Designation: ");
                scanf("%s", Designation);
                printf("Sal: ");
                scanf("%f", &Sal);
                printf("PhNo: ");
                scanf("%s", PhNo);
                Employee* newNode = createNode(SSN, Name, Dept, Designation, Sal, PhNo);
                insertAtEnd(&head, newNode);
                break;
            }
            case 2: 
                displayDLL(head); 
                break;
            case 3: 
                deleteAtEnd(&head); 
                break;
            case 4: {
                int SSN;
                char Name[50], Dept[50], Designation[50], PhNo[20];
                float Sal;
                printf("Enter details for new employee:\n");
                printf("SSN: ");
                scanf("%d", &SSN);
                printf("Name: ");
                scanf("%s", Name);
                printf("Dept: ");
                scanf("%s", Dept);
                printf("Designation: ");
                scanf("%s", Designation);
                printf("Sal: ");
                scanf("%f", &Sal);
                printf("PhNo: ");
                scanf("%s", PhNo);
                Employee* newNode = createNode(SSN, Name, Dept, Designation, Sal, PhNo);
                insertAtFront(&head, newNode);
                break;
            }
            case 5: 
                deleteAtFront(&head); 
                break;
            case 6: 
                demoDEQueue(head); 
                break;
            case 7: 
                exit(0);
            default: 
                printf("Invalid choice! Please try again.\n");
        }
    }
}
