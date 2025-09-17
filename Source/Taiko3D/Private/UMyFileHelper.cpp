// Fill out your copyright notice in the Description page of Project Settings.


#include "UMyFileHelper.h"
#include "Misc/FileHelper.h"
#include "Misc/Paths.h"

bool UMyFileHelper::LoadTextFileToStringArray(const FString& FilePath, TArray<FString>& OutLines)
{
    return FFileHelper::LoadFileToStringArray(OutLines, *FilePath);
}
