// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "UMyFileHelper.generated.h"

/**
 * 
 */
UCLASS()
class UMyFileHelper : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
public:
	UFUNCTION(BlueprintCallable, Category = "File")
	static bool LoadTextFileToStringArray(const FString& FilePath, TArray<FString>& OutLines);
};
